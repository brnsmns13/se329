
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
    // Pull the inputs from the document
	var question = document.getElementById("question");
	var a = document.getElementById("a1");
	var b = document.getElementById("a2");
	var c = document.getElementById("a3");
	var d = document.getElementById("a4");
	var correct = 'a';
	
    // Create a new question and add it to the array
	var newQuestion = quizQuestion(
        question.value,
        a.value,
        b.value,
        c.value,
        d.value,
        correct);
	questionArr.push(newQuestion);

    // Add question title to list for user
    var q_list = document.getElementById('question-list');
    var li = document.createElement('li');
    li.className = "list-group-item";
    li.appendChild(document.createTextNode(question.value));
    q_list.appendChild(li);

    // Clear the fields
    question.value = "";
    a.value = "";
    b.value = "";
    c.value = "";
    d.value = "";

	return false;
}

function clearArr(){
	questionArr = [];
	alert("cleared");
}

function toJSON(){
	var data = {
		"questions" : questionArr,
        "name": quizName
	};
	
	$.post("/create", JSON.stringify(data));

    // If we let the post redirect then we can fix the reload error
    window.location.replace("/quizzes");
}
