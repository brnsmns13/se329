
var questionArr = [];

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

function getFormData(){
	

	var question = document.getElementById("element_1").value;
	var a = document.getElementById("element_2").value;
	var b = document.getElementById("element_3").value;
	var c = document.getElementById("element_4").value;
	var d = document.getElementById("element_5").value;
	var correct = document.getElementById("element_6_1").value;
	
	var newQuestion = quizQuestion(question, a,b,c,d, correct);
	questionArr.push(newQuestion);
	console.log(newQuestion);
	console.log(questionArr);
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
	
	$.post("/create", data);
}