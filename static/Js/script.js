document.addEventListener('DOMContentLoaded', function() {
    let submitButton = document.getElementById('submit-btn');
    let twitterForm = document.getElementById('twitter-form');
    let checkTweetButton = document.getElementById('check-tweet');
    let messageDiv = document.getElementById('message');
    let timer = null;

    // Timer to prevent multiple submissions within 15 minutes
    function startTimer() {
        let countdown = 900; // 15 minutes
        submitButton.disabled = true;

        timer = setInterval(function() {
            countdown--;
            if (countdown <= 0) {
                clearInterval(timer);
                submitButton.disabled = false;
                messageDiv.innerHTML = 'You can now submit another comment!';
            } else {
                messageDiv.innerHTML = `Please wait for ${Math.floor(countdown / 60)}:${countdown % 60 < 10 ? '0' + countdown % 60 : countdown % 60} minutes.`;
            }
        }, 1000);
    }

    // Handle Twitter form submission
    twitterForm.addEventListener('submit', function(e) {
        e.preventDefault();
        let tweetUrl = document.getElementById('tweet-url').value;
        fetch('/get_tweet_comments', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({url: tweetUrl})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                messageDiv.innerHTML = `Comments fetched!`;
                startTimer();
            } else {
                messageDiv.innerHTML = `Error: ${data.error}`;
            }
        });
    });
});
