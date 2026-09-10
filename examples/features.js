// SPDX-FileCopyrightText: 2026 Sebastien Rousseau <sebastian.rousseau@gmail.com>
// SPDX-License-Identifier: Apache-2.0 OR MIT

/**
 * 100% Feature Showcase for @sebastienrousseau/prettier-config
 */
const config = require("../index.cjs");
const assert = require("assert");

console.log(
  "=== 100% Feature Showcase: @sebastienrousseau/prettier-config ===",
);
assert(typeof config.$schema === "string");
assert.strictEqual(config.tabWidth, 2);
assert.strictEqual(config.useTabs, false);
assert.strictEqual(config.semi, true);
assert.strictEqual(config.singleQuote, false);
assert.strictEqual(config.endOfLine, "lf");
assert.strictEqual(config.trailingComma, "all");

console.log("  ✓ Tab width:", config.tabWidth);
console.log("  ✓ Trailing commas: all");
console.log("  ✓ Line endings: lf");
console.log("✅ 100% of prettier-config formatting rules validated.");
