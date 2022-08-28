#!/bin/sh

certoraRun \
    contracts/ERC20.sol                    \
    --verify ERC20:certora/spec/ERC20.spec \
    --solc solc-0.8.0                      \
    --msg "ERC20 verification"             \
    $*

