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
        pkgs = import nixpkgs { inherit system; };
        packages = with pkgs; [
          python3
          pandoc
          wkhtmltopdf-bin
          html-minifier
          clean-css-cli
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
