
var questionArr = [];
var quizName = '';

function quizQuestion(q,a,b,c,d,ans){
	var question = {};
	question.question = q;
	question.a = a;
	question.b = b;
	question.c = c;
	question.d = d;
	question.correctAnswer = ans;
	return question;
}

function create() {
    quizName = document.getElementById("quiz-name").value;
    document.getElementById("quiz-name-view").style.display = "none";
    document.getElementById("quiz-questions-view").style.display = "";
    document.getElementById("quiz-name-header").textContent = "Quiz: " + quizName;

    return false;
}

function getFormData(){
	var question = document.getElementById("question").value;
	var a = document.getElementById("a1").value;
	var b = document.getElementById("a2").value;
	var c = document.getElementById("a3").value;
	var d = document.getElementById("a4").value;
	var correct = 'a';
	
	var newQuestion = quizQuestion(question, a,b,c,d, correct);
	questionArr.push(newQuestion);

    var q_list = document.getElementById('question-list');
    var li = document.createElement('li');
    li.className = "list-group-item";
    li.appendChild(document.createTextNode(question));
    q_list.appendChild(li);

	return false;
}

function clearArr(){
	questionArr = [];
	alert("cleared");
}

function toJSON(){
	var data = {
		"questionArr" : questionArr
	};
	
	$.post("/create", JSON.stringify(data));
    window.location.replace("/quizzes");
}
