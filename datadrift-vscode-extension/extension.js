const vscode = require('vscode');

function activate(context) {
    let disposable = vscode.commands.registerCommand(
        'data-drift.launch',
        function () {
            vscode.window.showInformationMessage('Launching Data Drift...');

            // TODO: replace this with your actual EXE path later
            const { exec } = require('child_process');

            exec('dist/DataDrift/DataDrift.exe', (err) => {
                if (err) {
                    vscode.window.showErrorMessage('Failed to launch Data Drift');
                    console.error(err);
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