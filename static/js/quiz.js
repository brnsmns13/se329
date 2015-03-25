
var quizName = '';
var questions = [];
var answerIDs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var nextAnswer = 0;

function create() {
    quizName = document.getElementById("quiz-name").value;
    document.getElementById("quiz-name-view").style.display = "none";
    document.getElementById("quiz-questions-view").style.display = "";
    document.getElementById("quiz-name-header").textContent = "Quiz: " + quizName;
    addAnswer();
    return false;
}

function addAnswer() {
    if (nextAnswer >= answerIDs.length) {
        alert("Too many answers!");
        return false;
    }

    var answerID = answerIDs[nextAnswer];
    nextAnswer += 1;
    $('#answer-list').append(
        '<div class="form-group">\n' +
        '<label for="answer' + answerID + '">Answer ' + answerID +
        '</label>\n' +
        '<input type="text" class="form-control answer" ' +
        'placeholder="Answer ' + answerID + '"></input>\n' +
        '</div>\n');

    $('#answer-selector').append(
        '<label class="btn btn-primary" for="correct' + nextAnswer + '">\n' +
        '<input type="radio" name="correct-answer" value="' + answerID + '" ' +
        'autocomplete="off"></input> ' + answerID + '\n' +
        '</label>');

    return false;
}

function addQuestion() {
    // Pull the inputs from the document
	var questionField = $('#question');
    var question = questionField.val();

    var answers = {};
    var answerList = $('#answer-list');
	answerList.find('.answer').each(function(index, field) {
        answers[answerIDs[index]] = $(field).val();
    });

    var correctList = $('#answer-selector');
	var correctField = correctList.find(
        "input:radio[name ='correct-answer']:checked");

    var correct = correctField.val();
    if (!correct) {
        alert('Select a correct answer!');
        return false;
    }

    var newQuestion = {
        question: question,
        answers: answers,
        correctAnswer: correct
    };
	questions.push(newQuestion);

    // Add question title to list for user
    var qList = document.getElementById('question-list');
    var li = document.createElement('li');
    li.className = "list-group-item";
    li.appendChild(document.createTextNode(
        newQuestion.question + ' (' + correct + ': ' + answers[correct] + ')'));

    qList.appendChild(li);

    // Clear the fields
    questionField.val('');
    answerList.empty();
    correctList.empty();
    nextAnswer = 0;
    addAnswer();
    return false;
}

function submitQuiz() {
	var data = {
		"questions" : questions,
        "name": quizName
	};
	
	$.post("/create", JSON.stringify(data));

    // If we let the post redirect then we can fix the reload error
    window.location.replace("/quizzes");
}
