module.exports = {
    "env": {
        "browser": true,
        "commonjs": true,
        "es2021": true,
        "mocha": true,
    },
    "plugins": ["mocha"],
    "extends": "eslint:recommended",
    "overrides": [
        {
            "env": {
                "node": true
            },
            "files": [
                ".eslintrc.{js,cjs}"
            ],
            "parserOptions": {
                "sourceType": "script"
            }
        }
    ],
    "parserOptions": {
        "ecmaVersion": "latest"
    },
    "rules": {
    }
}
