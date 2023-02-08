drop table if exists respondents_weight;
drop view if exists respondents_weight_agg;

create table respondents_weight (
    idx int,
    Date date,
    respondent int2,
    Sex int2,
    Age int2,
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

create view respondents_weight_agg as
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