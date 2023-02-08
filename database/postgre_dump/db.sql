drop view if exists df_agg_view;
drop table if exists df_idx;
drop table if exists df_agg;

create table respondents_weight (
    idx int,
    Date date,
    respondent int,
    Sex int,
    Age int,
    Weight float
);

copy respondents_weight (
    idx,
    Date,
    respondent,
    Sex,
    Age,
    Weight
) from '/docker-entrypoint-initdb.d/OKKAM_Middle Python Developer_data.csv' delimiter ';' csv header;

alter table respondents_weight drop idx;

create table respondents_weight_agg as
    select
        respondent
        , Sex
        , Age
        , avg(weight) average_weight
    from
        respondents_weight
    group by
        respondent
        , Sex
        , Age;

create view respondents_weight_agg_view as
    select
        respondent
        , Sex
        , Age
        , avg(weight) average_weight
    from
        respondents_weight
    group by
        respondent
        , Sex
        , Age;
