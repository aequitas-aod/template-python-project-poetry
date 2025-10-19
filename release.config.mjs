let dryRun = (process.env.RELEASE_DRY_RUN || "false").toLowerCase() === "true";
let testPypi = (process.env.RELEASE_TEST_PYPI || "false").toLowerCase() === "true";
let pypiUsername = process.env.PYPI_USERNAME;
let pypiPassword = process.env.PYPI_PASSWORD;

if (!pypiUsername || !pypiPassword) {
    dryRun = true;
    console.warn("PYPI_USERNAME or PYPI_PASSWORD not set. Running in dry-run mode.");
}

let prepareCmd = "poetry version -- \${nextRelease.version}";
let publishCmd = `poetry publish --build --username ${pypiUsername} --password ${pypiPassword}`;

if (testPypi) {
    // test-pypi repository name is defined in poetry.toml
    publishCmd = publishCmd.replace("--build", "--build --repository pypi-test");
}

if (dryRun) {
    publishCmd = publishCmd.replace("--build", "--build --dry-run");
}

import config from 'semantic-release-preconfigured-conventional-commits' with {type: 'json'};

config.plugins.push(
    ["@semantic-release/exec", {
        "prepareCmd" : prepareCmd,
        "publishCmd": publishCmd,
    }]
)

if (!dryRun) {
    config.plugins.push(
        ["@semantic-release/github", {
            "assets": [
                { "path": "dist/*" },
            ]
        }],
        ["@semantic-release/git", {
            "assets": [
                "CHANGELOG.md",
                "pyproject.toml"
            ],
            "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
        }]
    );
}

export default config;
