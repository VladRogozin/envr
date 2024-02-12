function checkAnswer() {
    var userAnswer = document.getElementById('user-answer').value.trim().toLowerCase();
    var correctAnswer = document.getElementById('user-answer').getAttribute('data-random-text');

    var feedbackElement = document.getElementById('feedback');
    var feedbackMessage = '';

    var userAnswerFoTest = userAnswer.replace(/[.,!?]/g, '');
    var correctAnswerFoTest = correctAnswer.replace(/[.,!?]/g, '');

    if (userAnswerFoTest === correctAnswerFoTest) {
        feedbackElement.innerHTML = '<strong class="text-success">Правильно!</strong>';
    } else {
        var userCorectWordsArray = userAnswer.split(' ');
        var userWordsArray = userAnswer.split(' ').map(word => word.replace(/[.,!?]/g, ''));
        var correctWordsArray = correctAnswer.split(' ').map(word => word.replace(/[.,!?]/g, ''));

        function removeDuplicates(array1, array2, userWord) {
            let trueArray = array1.filter(word => !array2.includes(word));
            for (var j = 0; j < trueArray.length; j++) {
                if (trueArray[j].length >= 2 && userWord.length >= 2) {
                    var firstTwoOfWord1 = trueArray[j].slice(0, 2);
                    var lastTwoOfWord2 = userWord.slice(0, 2);

                    if (firstTwoOfWord1 === lastTwoOfWord2) {
                        return true;
                    }
                }
            }
            return false;
        }

        // Использование функции removeDuplicates в вашем цикле
        for (var i = 0; i < userWordsArray.length; i++) {
            if (correctWordsArray.includes(userWordsArray[i])) {
                feedbackMessage += '<span style=" color: #3b3838;">' + userCorectWordsArray[i] + '</span> ';
            } else if (removeDuplicates(correctWordsArray, userWordsArray, userWordsArray[i])) {
                feedbackMessage += '<span class="" style=" color: #e9ed6d;">' + userCorectWordsArray[i] + '</span> ';
            } else if (correctWordsArray.indexOf(userWordsArray[i]) === -1) {
                // Если слово не совпадает, добавляем красное выделение
                feedbackMessage += '<span class="" style=" color: #cf1111;">' + userCorectWordsArray[i] + '</span> ';
            }
        }

        feedbackElement.innerHTML = '<strong style=" color: #3b3838;">' + feedbackMessage + '</strong>';
    }
}

function toggleHint(elementId, secondID) {
    var element = document.getElementById(elementId);
    element.style.display = (element.style.display === 'none') ? 'block' : 'none';

    if (secondID) {
        var elementSecond = document.getElementById(secondID);
        elementSecond.style.display = (elementSecond.style.display === 'none') ? 'block' : 'none';
    }
}