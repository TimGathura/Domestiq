//Code to dynamically update the tags
//Code with all features and all dropdowns
var selectedValues = {
    roles: null,
    location: null,
    gender: null,
    age: null
};

function updateTextBox(value, category) {
    var resultTextBox = document.getElementById('tagsTextbox');

    // Check if the category is roles, location, gender, or live
    if (category in selectedValues) {
        // Update the selected value for the category
        selectedValues[category] = value;

        // Remove existing tags for the category
        removeTags(category);

        // Create a new tag container
        var tagContainer = document.createElement('div');
        tagContainer.className = 'tagContainer';

        // Display the content
        tagContainer.innerHTML = value;

        // Create a delete button (x)
        var deleteButton = document.createElement('span');
        deleteButton.className = 'deleteTag';
        deleteButton.innerHTML = 'x';
        deleteButton.onclick = function () {
            // Remove the tag container and reset the selected value
            resultTextBox.removeChild(tagContainer);
            selectedValues[category] = null;
        };

        // Append the delete button to the tag container
        tagContainer.appendChild(deleteButton);

        // Append the tag container to the result text box
        resultTextBox.appendChild(tagContainer);

        // Order the tags in the logical order
        orderTags();
    }
}

function removeTags(category) {
    var resultTextBox = document.getElementById('tagsTextbox');

    // Remove existing tags for the category
    var existingTags = document.querySelectorAll('.tagContainer');
    existingTags.forEach(function (tag) {
        if (tag.textContent === selectedValues[category]) {
            resultTextBox.removeChild(tag);
        }
    });
}

function orderTags() {
    var resultTextBox = document.getElementById('tagsTextbox');

    // Get all tag containers
    var tags = Array.from(resultTextBox.querySelectorAll('.tagContainer'));

    // Sort the tags based on their categories
    tags.sort(function (a, b) {
        var categoryA = getCategory(a.textContent);
        var categoryB = getCategory(b.textContent);

        return getCategoryOrder(categoryA) - getCategoryOrder(categoryB);
    });

    // Clear the resultTextBox and append the sorted tags
    resultTextBox.innerHTML = '';
    tags.forEach(function (tag) {
        resultTextBox.appendChild(tag);
    });

    // Add the "Clear All" button if more than one tag is selected
    if (tags.length > 1) {
        addClearAllButton();
    } else {
        removeClearAllButton();
    }
}

function getCategory(value) {
    for (var category in selectedValues) {
        if (selectedValues[category] === value) {
            return category;
        }
    }
    return null;
}

function getCategoryOrder(category) {
    var order = {
        roles: 1,
        location: 2,
        gender: 3,
        age: 4
    };

    return order[category] || 0;
}

function addClearAllButton() {
    var resultTextBox = document.getElementById('tagsTextbox');
    var clearAllButton = document.getElementById('clearAllButton');

    // Add the "Clear All" button if not already added
    if (!clearAllButton) {
        clearAllButton = document.createElement('span');
        clearAllButton.id = 'clearAllButton';
        clearAllButton.className = 'deleteTag';
        clearAllButton.innerHTML = 'Clear All';
        clearAllButton.onclick = function () {
            // Remove all tags and reset selected values
            resultTextBox.innerHTML = '';
            for (var category in selectedValues) {
                selectedValues[category] = null;
            }
            removeClearAllButton();
        };

        resultTextBox.appendChild(clearAllButton);
    }
}

function removeClearAllButton() {
    var clearAllButton = document.getElementById('clearAllButton');

    // Remove the "Clear All" button if it exists
    if (clearAllButton) {
        clearAllButton.parentNode.removeChild(clearAllButton);
    }
}