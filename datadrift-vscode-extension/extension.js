const vscode = require('vscode');
const { exec } = require('child_process');
const path = require('path');

function activate(context) {

    console.log("Data Drift Sidebar Extension Active");

    // Command fallback
    const command = vscode.commands.registerCommand(
        'data-drift.launch',
        () => launchGame()
    );

    context.subscriptions.push(command);

    // Sidebar provider
    const provider = new BreakViewProvider();
    vscode.window.registerTreeDataProvider('datadriftView', provider);
}

function launchGame() {
    // FIX: EXE is in root folder, NOT dist/
    const exePath = path.join(__dirname, 'DataDrift.exe');

    exec(`"${exePath}"`, (err) => {
        if (err) {
            vscode.window.showErrorMessage("Failed to launch DataDrift.exe");
            console.error(err);
        }
    });
}

class BreakViewProvider {
    getTreeItem(element) {
        return element;
    }

    getChildren() {
        return [
            new BreakItem("▶ Play Data Drift")
        ];
    }
}

class BreakItem extends vscode.TreeItem {
    constructor(label) {
        super(label);

        this.command = {
            command: "data-drift.launch",
            title: "Play Data Drift"
        };

        this.iconPath = new vscode.ThemeIcon("play");
    }
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};