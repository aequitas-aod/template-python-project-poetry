var publishCmd = `
python -m build
python -m twine upload dist/*
`
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
