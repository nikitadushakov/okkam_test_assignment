let a1_input = document.querySelector(".au1 input");
let a2_input = document.querySelector(".au2 input");
// console.dir(a1_input);
let button = document.querySelector(".button");
let result = document.querySelector(".result");

const get_percent = async (audience_1, audience_2) => {
    let res = await fetch(`${window.origin}/getPercent?audience1=${audience_1}&audience2=${audience_2}`);
    let json = await res.json()
    return json['percent']
}
button.addEventListener("click", async (e) => {
    if(!a1_input.value || !a2_input.value) {
        result.innerHTML = 'no audiences values';
        return
    }
    let res = await get_percent(a1_input.value, a2_input.value); 
    result.innerHTML = res;
});
