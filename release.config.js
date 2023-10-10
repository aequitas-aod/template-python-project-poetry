var dryRun = (process.env.RELEASE_DRY_RUN || "false").toLowerCase() === "true";

var publishCmd = `
python -m build
python -m twine upload dist/*
`

if (dryRun) {
    publishCmd = publishCmd.replace("upload", "upload --repository testpypi");
}

var config = require('semantic-release-preconfigured-conventional-commits');

config.plugins.push(
    [
        "@semantic-release/exec",
        {
            "publishCmd": publishCmd,
        }
    ],
    ["@semantic-release/github", {
        "assets": [ 
            { "path": "dist/*" },
         ]
    }],
    "@semantic-release/git",
)

module.exports = config
