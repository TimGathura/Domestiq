/*
// Tabs functionality
function showContent(contentId) {
    // Get all content sections
    var contentSections = document.querySelectorAll('.content-section');

    // Hide all content sections
    contentSections.forEach(function (section) {
        section.style.display = 'none';
    });

    // Show the selected content section
    var selectedContent = document.getElementById(contentId);
    if (selectedContent) {
        selectedContent.style.display = 'block';
    }

    // Get all tab links
    var tabLinks = document.querySelectorAll('#tabs a');

    // Remove the 'active' class from all tab links
    tabLinks.forEach(function (link) {
        link.classList.remove('active');
    });

    // Find the corresponding tab link and add the 'active' class
    var activeTabLink = document.querySelector(`#tabs a[href="javascript:void(0);" onclick="showContent('${contentId}')"]`);
    if (activeTabLink) {
        activeTabLink.classList.add('active');
    }
} */


// Tabs functionality
function showContent(contentId) {
    // Get all content sections
    var contentSections = document.querySelectorAll('.content-section');

    // Hide all content sections
    contentSections.forEach(function (section) {
        section.style.display = 'none';
    });

    // Show the selected content section
    var selectedContent = document.getElementById(contentId);
    if (selectedContent) {
        selectedContent.style.display = 'block';
    }

    // Get all tab links
    var tabLinks = document.querySelectorAll('#tabs a');

    // Remove the 'active' class from all tab links
    tabLinks.forEach(function (link) {
        link.classList.remove('active');
    });

    // Find the corresponding tab link and add the 'active' class
    var activeTabLink = document.querySelector(`#tabs a[href="#${contentId}"]`);
    if (activeTabLink) {
        activeTabLink.classList.add('active');
    }
}
