function setValue(text) {
    var textarea = document.getElementById("answerInput");
    textarea.placeholder = text;
    textarea.style.height = textarea.scrollHeight + "px";
}

function GetStringView(number, isChecked) {
    console.log(number, isChecked);
    var answer = "Unexpected error"
    var response = fetch('http://localhost:8000/', {
        method: 'POST',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        body: JSON.stringify({ "number": number, "checked": isChecked })
    })
        .then(response => response.text())
        .then(text => { answer = text; setValue(answer); })
        .catch(error => console.error(error));

    //document.getElementById("answerInput").placeholder = answer;
}

var submitBtn = document.getElementById("SubmitBtn");
submitBtn.addEventListener("click", () => GetStringView(
    document.getElementById("exampleInputNumber").value,
    document.getElementById("exampleCheck1").checked)
);

var form = document.getElementById("form1");
form.addEventListener("keypress", function (e) {
    if (e.keyCode == 13) {
        e.preventDefault();
        return false;
    }
})