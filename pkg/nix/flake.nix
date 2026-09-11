{
  description = "Shareable Prettier configuration rules adhering to modern formatting standards";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAll = f: nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
    in
    {
      packages = forAll (pkgs: {
        default = pkgs.stdenv.mkDerivation {
          pname = "node-sebastienrousseau-prettier-config";
          version = "0.0.7";
          src = ../..;

          # Inert data plus a loader: nothing to build, nothing to strip.
          dontBuild = true;
          dontStrip = true;

          installPhase = ''
            runHook preInstall
            out_dir="$out/lib/node_modules/@sebastienrousseau/prettier-config"
            mkdir -p "$out_dir"
            cp package.json index.js index.mjs index.cjs index.d.ts LICENSE .editorconfig "$out_dir/"
            runHook postInstall
          '';

          meta = with pkgs.lib; {
            description = "Shareable Prettier configuration rules adhering to modern formatting standards";
            homepage = "https://github.com/sebastienrousseau/prettier-config";
            license = with licenses; [ asl20 mit ];
            platforms = platforms.all;
          };
        };
      });

      checks = forAll (pkgs: {
        loads = pkgs.runCommand "prettier-config-loads" { buildInputs = [ pkgs.nodejs_20 ]; } ''
          node -e 'const c = require("${self.packages.${pkgs.system}.default}/lib/node_modules/@sebastienrousseau/prettier-config");
                   if (typeof c !== "object") { throw new Error("preset did not load as an object"); }'
          touch $out
        '';
      });
    };
}
