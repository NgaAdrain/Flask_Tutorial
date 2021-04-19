var callCounter;
var qnumber;
function pushQuestion() {
    var con3 = document.getElementById("showQuestion");
    con3.style.display = 'none';
    qnumber = document.getElementById("Qnumber");
    var saveQuestion = 
        {'question':document.getElementById( "Qtext" ).value,
        'one':document.getElementById( "select1" ).value,
        'two':document.getElementById( "select2" ).value,
        'three':document.getElementById( "select3" ).value,
        'four':document.getElementById( "select4" ).value,
        'five':document.getElementById( "select5" ).value,
        'answer':document.getElementById( "Qanswer" ).value,
        'explanation':document.getElementById( "Explanation" ).value};
    if (document.getElementById( "Qnumber" ).value != '' && document.getElementById( "Qtext" ).value != '' &&
    document.getElementById( "select1" ).value != '' && document.getElementById( "select2" ).value != '' &&
    document.getElementById( "select3" ).value != '' && document.getElementById( "select4" ).value != '' &&
    document.getElementById( "select5" ).value != '' && document.getElementById( "Qanswer" ).value != '') 
    {
        localStorage.setItem(qnumber.value, JSON.stringify(saveQuestion));
        alert((qnumber.value)+"번 문제가 저장되었습니다.");
        var con = document.getElementById('make');
        if(con.style.display=='none'){
             con.style.display = 'block';
        }else{
            con.style.display = 'none';
        }
    }
    
}

function callQuestion() {
    callCounter = document.getElementById( "Callcounter" );
    var callnum = callCounter.value;
    callnum--;
    if (localStorage.getItem(JSON.parse(callnum))!=null) {
        alert(localStorage.getItem(JSON.parse(callnum)));
    }
    else {
        alert("저장된 문제가 없습니다.");
    }
}

function show(char) {
    var con = document.getElementById(char);
    if(con.style.display=='none'){
        con.style.display = 'block';
    }else{
        con.style.display = 'none';
    }
    var number = document.getElementById("Qnumber");
    number.value = null;
    var con2 = document.getElementById("showQuestion");
    con2.style.display = 'none';
    var Qtext = document.getElementById("Qtext");
    var QtextValue = null;
    Qtext.value = QtextValue;
    var select1 = document.getElementById("select1");
    select1.value = null;
    var select2 = document.getElementById("select2");
    select2.value = null;
    var select3 = document.getElementById("select3");
    select3.value = null;
    var select4 = document.getElementById("select4");
    select4.value = null;
    var select5 = document.getElementById("select5");
    select5.value = null;
    var explanation = document.getElementById("Explanation");
    explanation.value = null;
    var answer = document.getElementById("Qanswer");
    answer.value = null;
}

function print_question() {
    var text = "";
    for (var i = 1; i < 10;i++) {
        var array = JSON.parse(localStorage.getItem(i));
        if (array!= null) {
            text += i+"번 - "+ JSON.stringify(array.explanation) + " <button onclick =\"showQuestion(" + i
            + ")\" >확인</button>" + " <button onclick =\"changeQuestion("+ i +")\" >편집</button>" + "<p>";
        }
        document.getElementById( "showQuestion" ).innerHTML = text;
    }
    var con = document.getElementById("showQuestion");
    if(con.style.display=='none'){
        con.style.display = 'block';
    }else{
        con.style.display = 'none';
    }
    var con2 = document.getElementById("make");
    con2.style.display = 'none';
}

function showQuestion(int) {
    var con = document.getElementById("showQuestion");
    con.style.display ='none';
    var con2 = document.getElementById("make");
    con2.style.display = 'block';
    var con3 = document.getElementById("pushbutton");
    con3.style.display ='none';
    var con4 = document.getElementById("pushanswer");
    con4.style.display ='block';
    var array = localStorage.getItem(int);
    var Qnumber = document.getElementById("Qnumber");
    Qnumber.value = int;
    var Qtext = document.getElementById("Qtext");
    var QtextValue = JSON.parse(array).question;
    Qtext.value = QtextValue;
    var select1 = document.getElementById("select1");
    select1.value = JSON.parse(array).one;
    var select2 = document.getElementById("select2");
    select2.value = JSON.parse(array).two;
    var select3 = document.getElementById("select3");
    select3.value = JSON.parse(array).three;
    var select4 = document.getElementById("select4");
    select4.value = JSON.parse(array).four;
    var select5 = document.getElementById("select5");
    select5.value = JSON.parse(array).five;
    var explanation = document.getElementById("Explanation");
    explanation.value = JSON.parse(array).explanation;
    var answer = document.getElementById("Qanswer");
    answer.value = null;
}

function pushAnswer() {
    var Qnumber = document.getElementById("Qnumber").value;
    var answer = "\""+String(document.getElementById( "Qanswer" ).value)+"\"";
    var Qanswer = JSON.parse(localStorage.getItem(Qnumber));
    if (answer != null) {
        var questionAnswer = JSON.stringify(Qanswer.answer)
        if (answer == questionAnswer) {
            alert("정답입니다");
        }
        else {
            alert("오답입니다");
        }
    }
}

function changeQuestion(int) {
    var con = document.getElementById("showQuestion");
    con.style.display ='none';
    var con2 = document.getElementById("make");
    con2.style.display = 'block';
    var con3 = document.getElementById("pushbutton");
    con3.style.display ='block';
    var con4 = document.getElementById("pushanswer");
    con4.style.display ='none';
    var array = localStorage.getItem(int);
    var Qnumber = document.getElementById("Qnumber");
    Qnumber.value = int;
    var Qtext = document.getElementById("Qtext");
    var QtextValue = JSON.parse(array).question;
    Qtext.value = QtextValue;
    var select1 = document.getElementById("select1");
    select1.value = JSON.parse(array).one;
    var select2 = document.getElementById("select2");
    select2.value = JSON.parse(array).two;
    var select3 = document.getElementById("select3");
    select3.value = JSON.parse(array).three;
    var select4 = document.getElementById("select4");
    select4.value = JSON.parse(array).four;
    var select5 = document.getElementById("select5");
    select5.value = JSON.parse(array).five;
    var explanation = document.getElementById("Explanation");
    explanation.value = JSON.parse(array).explanation;
    var answer = document.getElementById("Qanswer");
    answer.value = JSON.parse(array).answer;
    var con3 = document.getElementById("pushbutton");
    con3.style.display ='block';
    var con4 = document.getElementById("pushanswer");
    con4.style.display ='none';
}