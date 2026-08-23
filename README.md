<!-- SPDX-License-Identifier: Apache-2.0 OR MIT>

<p align="center">
  <img src="./prettier-config.svg" alt="prettier-config logo" width="128" />
</p>

<h1 align="center">@sebastienrousseau/prettier-config</h1>

<p align="center">
  Shareable Prettier configuration adhering to modern code formatting standards.
</p>

<p align="center">
  <a href="https://github.com/sebastienrousseau/prettier-config/actions"><img src="https://img.shields.io/github/actions/workflow/status/sebastienrousseau/prettier-config/ci.yml?branch=main&style=for-the-badge&logo=github" alt="Build Status" /></a>
  <a href="https://www.npmjs.com/package/@sebastienrousseau/prettier-config"><img src="https://img.shields.io/npm/v/@sebastienrousseau%2Fprettier-config?style=for-the-badge&color=fc8d62&logo=npm" alt="npm package" /></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/sebastienrousseau/prettier-config"><img src="https://img.shields.io/ossf-scorecard/github.com/sebastienrousseau/prettier-config?style=for-the-badge&label=OpenSSF%20Scorecard&logo=openssf" alt="OpenSSF Scorecard" /></a>
  <a href="https://github.com/sebastienrousseau/prettier-config/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-ISC-blue?style=for-the-badge" alt="License" /></a>
</p>

---

## Contents

**Getting Started**
- [Installation](#installation) — Package manager commands
- [Quick Start](#quick-start) — Configure in under a minute

**Features & Rule Showcase**
- [Consistent Code Formatting](#consistent-code-formatting) — Code comparison
- [Module Compatibility](#module-compatibility) — Dual CJS/ESM & TypeScript declarations

**Governance & Quality**
- [Development & Testing](#development--testing) — Local validation
- [Security & Compliance](#security--compliance) — SLSA attestation & vulnerability policy
- [Author & License](#author--license) — Open source license

---

## Installation

Install using your preferred package manager:

```bash
# npm
npm install --save-dev @sebastienrousseau/prettier-config

# pnpm
pnpm add -D @sebastienrousseau/prettier-config

# yarn
yarn add -D @sebastienrousseau/prettier-config

# bun
bun add -d @sebastienrousseau/prettier-config
```

---

## Quick Start

### In `package.json`

```json
{
  "prettier": "@sebastienrousseau/prettier-config"
}
```

### In CommonJS Configuration

```js
module.exports = require("@sebastienrousseau/prettier-config");
```

### In ES Module Configuration

```js
import config from "@sebastienrousseau/prettier-config";
export default config;
```

---

## Consistent Code Formatting

Configures 80-character print width, double quotes, trailing commas, and LF line endings.

### Before (Unstandardized)

```javascript
function foo(a,b){
return a+b}
```

### After (@sebastienrousseau/prettier-config Enforced)

```javascript
function foo(a, b) {
  return a + b;
}
```

---

## Module Compatibility

This package exports dual module entrypoints via `package.json` `exports`:

```json
"exports": {
  ".": {
    "types": "./index.d.ts",
    "import": "./index.mjs",
    "require": "./index.cjs"
  }
}
```

Full TypeScript definitions (`index.d.ts`) are included for rich IDE autocomplete and inline JSDoc tooltips.

---

## Development & Testing

```bash
# Clone repository
git clone https://github.com/sebastienrousseau/prettier-config.git
cd prettier-config

# Run validation tests
npm test
```

---

## Security & Compliance

- **SLSA Level 3 Provenance**: Builds are cryptographically signed with keyless provenance via GitHub Actions.
- **Automated Security Audit**: Monitored continuously with CodeQL and Dependabot.
- **Commit Signatures**: All commits are SSH/GPG signed.
- See [SECURITY.md](SECURITY.md) for vulnerability reporting procedures.

---

## Author & License

Developed and maintained by **[Sebastien Rousseau](https://github.com/sebastienrousseau)**.

Released under the [ISC License](LICENSE).
