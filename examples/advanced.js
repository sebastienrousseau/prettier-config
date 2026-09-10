// SPDX-FileCopyrightText: 2026 Sebastien Rousseau <sebastian.rousseau@gmail.com>
// SPDX-License-Identifier: Apache-2.0 OR MIT

/**
 * Advanced custom Prettier configuration
 */
const base = require("../index.cjs");
const custom = { ...base, printWidth: 100, singleQuote: true };
console.log("Custom printWidth:", custom.printWidth);
