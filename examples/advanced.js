/**
 * Advanced custom Prettier configuration
 */
const base = require("../index.cjs");
const custom = { ...base, printWidth: 100, singleQuote: true };
console.log("Custom printWidth:", custom.printWidth);
