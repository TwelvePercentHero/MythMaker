$(document).ready(function() {
    $("#show-videos").click(function() {
        $("#video-results").removeClass("d-none").addClass("d-block");
        $("#story-results").removeClass("d-block").addClass("d-none");
        $("#audio-results").removeClass("d-block").addClass("d-none");
        $("#user-results").removeClass("d-block").addClass("d-none");
    });
    $("#show-stories").click(function() {
        $("#video-results").removeClass("d-block").addClass("d-none");
        $("#story-results").removeClass("d-none").addClass("d-block");
        $("#audio-results").removeClass("d-block").addClass("d-none");
        $("#user-results").removeClass("d-block").addClass("d-none");
    });
    $("#show-audios").click(function() {
        $("#video-results").removeClass("d-block").addClass("d-none");
        $("#story-results").removeClass("d-block").addClass("d-none");
        $("#audio-results").removeClass("d-none").addClass("d-block");
        $("#user-results").removeClass("d-block").addClass("d-none");
    });
    $("#show-stories").click(function() {
        $("#video-results").removeClass("d-block").addClass("d-none");
        $("#story-results").removeClass("d-block").addClass("d-none");
        $("#audio-results").removeClass("d-block").addClass("d-none");
        $("#user-results").removeClass("d-none").addClass("d-block");
    });
    
});