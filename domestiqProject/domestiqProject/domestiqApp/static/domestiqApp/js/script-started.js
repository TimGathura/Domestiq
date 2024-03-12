// 1. Get Started button link
document.addEventListener('DOMContentLoaded', function () {
    // Get the button element
    const getStartedButton = document.querySelector('.get-started-btn');

    // Add click event listener to the button
    getStartedButton.addEventListener('click', function () {
        // Redirect to the get-started.html page
        window.location.href = 'get-started.html';
    });
});

//2. Log In button link
document.addEventListener('DOMContentLoaded', function() {
    //Get the log in button element
    const logInButton = document.querySelector('.log-in-btn');

    //Add click event listener to the button
    logInButton.addEventListener('click', function() {
        //Redirect to the log-in.html page
        window.location.href = 'log-in.html';
    });
});


//3. Toggle registration form visibility
function toggleForm(showForm, hideForm) {
    document.getElementById(showForm).style.display = 'block';
    document.getElementById(hideForm).style.display = 'none';

    // Toggle active class on buttons
    document.getElementById(showForm + '-btn').classList.add('active');
    document.getElementById(hideForm + '-btn').classList.remove('active');
}





//4. DOB functionality
//All day values dynamically change depending on the month
//Leap year functionality included 
function updateDays(monthId, dayId, yearId) {
    var monthSelect = document.getElementById(monthId);
    var daySelect = document.getElementById(dayId);
    var yearSelect = document.getElementById(yearId);

    // Get selected values
    var selectedMonth = parseInt(monthSelect.value);
    var selectedYear = parseInt(yearSelect.value);

    // Clear existing options
    daySelect.innerHTML = '';

    // Function to check if a year is a leap year
    function isLeapYear(year) {
        return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
    }

    // Define days in each month
    var daysInMonth = {
        1: 31, // January
        2: isLeapYear(selectedYear) ? 29 : 28, // February
        3: 31, // March
        4: 30, // April
        5: 31, // May
        6: 30, // June
        7: 31, // July
        8: 31, // August
        9: 30, // September
        10: 31, // October
        11: 30, // November
        12: 31  // December
    };

    // Populate days based on the selected month
    for (var i = 1; i <= daysInMonth[selectedMonth]; i++) {
        var option = document.createElement('option');
        option.value = i;
        option.text = i;
        daySelect.add(option);
    }
}

// Function to dynamically populate years from 1924 to 2006
function populateYears(yearId) {
    var yearSelect = document.getElementById(yearId);

    // Clear existing options
    yearSelect.innerHTML = '';

    // Populate years from 1924 to 2006
    for (var i = 1924; i <= 2006; i++) {
        var option = document.createElement('option');
        option.value = i;
        option.text = i;
        yearSelect.add(option);
    }
}

// Event listener for month change on client form
document.getElementById('month-c').addEventListener('change', function() {
    updateDays('month-c', 'day-c', 'year-c');
});

// Event listener for month change on worker form
document.getElementById('month-w').addEventListener('change', function() {
    updateDays('month-w', 'day-w', 'year-w');
});

// Initial update to set days based on the default month and year
updateDays('month-c', 'day-c', 'year-c');
updateDays('month-w', 'day-w', 'year-w');

// Populate years for both client and worker forms
populateYears('year-c');
populateYears('year-w');















