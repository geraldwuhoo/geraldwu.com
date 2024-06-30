{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config = {
            permittedInsecurePackages = [ "openssl-1.1.1w" ];
          };
        };
        packages = with pkgs; [
          python3
          pandoc
          wkhtmltopdf-bin
        ];
        pythonPackages = with pkgs.python3Packages; [
          jinja2
          pyyaml
          markdown
        ];
      in
      {
        devShells.default = pkgs.mkShell { buildInputs = packages ++ pythonPackages; };
      }
    );
}
