let editor;

async function onFormSubmit(event) {
    event.preventDefault();

    const logLevel = document.getElementById("logLevel");
    const logMessage = document.getElementById("logMessage");
    const enableLogExtraJSON = document.getElementById("enableLogExtraJSON");
    const status = document.getElementById("status");

    const requestBody = {
        level: logLevel.value,
        message: logMessage.value
    }

    try {
        if (enableLogExtraJSON.checked) {
            requestBody.extra = JSON.parse(editor.getValue())
        }

        const response = await fetch("/api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        });

        const responseJson = await response.json();
        console.log(responseJson);

        if (responseJson.message === "success") {
            status.innerHTML = "Success: " + responseJson.success;
            status.style.color = "green";
        } else {
            status.innerHTML = "Error: " + responseJson.error;
            status.style.color = "red";
        }
    } catch (err) {
        console.error("Error:", err);
        status.innerHTML = "Error: " + err.message;
        status.style.color = "red";
    }
}

function onFormReset(event) {
    disableEditor();
}

function disableEditor() {
    editor.setOption("readOnly", "nocursor");
    editor.getWrapperElement().classList.add("CodeMirror-disabled");
}

function enableEditor() {
    editor.setOption("readOnly", false);
    editor.getWrapperElement().classList.remove("CodeMirror-disabled");
}

function clickEnableLogExtraJSON() {
    const enableLogExtraJSON = document.getElementById("enableLogExtraJSON");
    const cursorPosition = document.getElementById('cursorPosition');

    if (enableLogExtraJSON.checked == true) {
        enableEditor();
        cursorPosition.style.opacity = 1;
    } else {
        disableEditor();
        cursorPosition.style.opacity = 0.6;
    }
}

function displayCursorPosition() {
    const cursorPosition = document.getElementById('cursorPosition');
    const cursor = editor.getCursor();
    const line = cursor.line + 1;
    const column = cursor.ch + 1;
    cursorPosition.textContent = `Ln: ${line}, Col: ${column}`;
}

async function contentLoaded() {
    const form = document.getElementById("formId");
    form.addEventListener("submit", onFormSubmit);
    form.addEventListener("reset", onFormReset);

    const enableLogExtraJSON = document.getElementById("enableLogExtraJSON");
    enableLogExtraJSON.addEventListener("click", clickEnableLogExtraJSON);

    editor = CodeMirror.fromTextArea(document.getElementById("logExtraJSON"), {
        mode: { name: "javascript", json: true },
        lineNumbers: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });

    editor.on("cursorActivity", displayCursorPosition);
    editor.setValue("{\"key\": \"value\"}\n");
    disableEditor();

    const cursorPosition = document.getElementById('cursorPosition');
    cursorPosition.style.opacity = 0.6;

    const status = document.getElementById("status");
    const logLevel = document.getElementById("logLevel");
    try {
        const response = await fetch("/api");

        const responseJson = await response.json();
        console.log(responseJson);

        const levels = ['debug', 'info', 'warning', 'error', 'critical'];
        for (let index = responseJson.log_level_number - 1; index < levels.length; index++) {
            const option = document.createElement("option");
            option.value = levels[index];
            option.text = levels[index].toUpperCase();
            logLevel.add(option);
        }
    } catch (err) {
        console.error("Error:", err);
        status.innerHTML = "Error: " + err.message;
        status.style.color = "red";
    }
}

document.addEventListener("DOMContentLoaded", contentLoaded);
