let display = document.getElementById("display");

function appendValue(val){
    if(display.innerText === "0"){
        display.innerText = val;
    } else {
        display.innerText += val;
    }
}

function clearDisplay(){
    display.innerText = "0";
}

function deleteLast(){
    display.innerText = display.innerText.slice(0,-1) || "0";
}

function calculate(){
    fetch("/calculate",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            expression: display.innerText
        })
    })
    .then(res => res.json())
    .then(data => {
        display.innerText = data.result;
    });
}