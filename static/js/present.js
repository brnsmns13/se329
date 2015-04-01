function displayQuiz(quiz_code, question_number){
    redirect("/start?quiz=" + quiz_code + "&question=" + question_number, 'post');
}

function redirect(url, method) {
    var form = $('<form>', {
        method: method,
        action: url
    }).submit();
}

function endQuiz(){
    window.location.replace("/quizzes");
}
