{
  description = "Rueben manages python and pydantic with nix flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/master";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
    let
    python = "python3";
    pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShell = pkgs.mkShell {
        buildInputs = [
          (pkgs.${python}.withPackages
            (ps: with ps; [
              pydantic 
            ]))
          pkgs.${python}
        ];
      };
    });
}
