---
title: "Usage — @sebastienrousseau/prettier-config"
description: "How to use and configure @sebastienrousseau/prettier-config."
layout: "doc"
---

# Usage

`@sebastienrousseau/prettier-config` can be consumed across all standard module formats.

## CommonJS

```javascript
module.exports = require("@sebastienrousseau/prettier-config");
```

## ES Modules

```javascript
import config from "@sebastienrousseau/prettier-config";
export default config;
```

## In `package.json`

```json
{
  "prettier": "@sebastienrousseau/prettier-config"
}
```
