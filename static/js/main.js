$(document).ready(function() {
    $("#show-videos").click(function() {
        $("#video-results").removeClass("d-none").addClass("d-block");
        $("#story-results").removeClass("d-block").addClass("d-none");
        $("#audio-results").removeClass("d-block").addClass("d-none");
        $("#user-results").removeClass("d-block").addClass("d-none");
        $("#show-videos").removeClass("deselected").addClass("selected");
        $("#show-stories").removeClass("selected").addClass("deselected");
        $("#show-audios").removeClass("selected").addClass("deselected");
        $("#show-users").removeClass("selected").addClass("deselected");
    });
    $("#show-stories").click(function() {
        $("#video-results").removeClass("d-block").addClass("d-none");
        $("#story-results").removeClass("d-none").addClass("d-block");
        $("#audio-results").removeClass("d-block").addClass("d-none");
        $("#user-results").removeClass("d-block").addClass("d-none");
        $("#show-videos").removeClass("selected").addClass("deselected");
        $("#show-stories").removeClass("deselected").addClass("selected");
        $("#show-audios").removeClass("selected").addClass("deselected");
        $("#show-users").removeClass("selected").addClass("deselected");
    });
    $("#show-audios").click(function() {
        $("#video-results").removeClass("d-block").addClass("d-none");
        $("#story-results").removeClass("d-block").addClass("d-none");
        $("#audio-results").removeClass("d-none").addClass("d-block");
        $("#user-results").removeClass("d-block").addClass("d-none");
        $("#show-videos").removeClass("selected").addClass("deselected");
        $("#show-stories").removeClass("selected").addClass("deselected");
        $("#show-audios").removeClass("deselected").addClass("selected");
        $("#show-users").removeClass("selected").addClass("deselected");
    });
    $("#show-users").click(function() {
        $("#video-results").removeClass("d-block").addClass("d-none");
        $("#story-results").removeClass("d-block").addClass("d-none");
        $("#audio-results").removeClass("d-block").addClass("d-none");
        $("#user-results").removeClass("d-none").addClass("d-block");
        $("#show-videos").removeClass("selected").addClass("deselected");
        $("#show-stories").removeClass("selected").addClass("deselected");
        $("#show-audios").removeClass("selected").addClass("deselected");
        $("#show-users").removeClass("deselected").addClass("selected");
    });
    
});