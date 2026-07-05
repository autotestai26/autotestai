pragma solidity ^0.8.13;

contract MiniCounter {
    uint256 public value;

    function increment() external {
        value += 1;
    }

    function reset() external {
        value = 0;
    }
}
