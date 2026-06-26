const vscode = require("vscode");
const { execFile } = require("child_process");
const path = require("path");

function activate(context) {
    let disposable = vscode.commands.registerCommand(
        "data-drift.launch",
        function () {

            const exePath = path.join(
                __dirname,
                "release",
                "v1.0.0",
                "DataDrift.exe"
            );

            execFile(exePath, (err) => {
                if (err) {
                    vscode.window.showErrorMessage("Failed to launch Data Drift");
                }
            });
        }
    );

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};