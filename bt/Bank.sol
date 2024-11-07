// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint256) public balanceOf;

    function deposit(uint256 amount) public {
        // require(msg.value == amount, "Amount sent must match the deposit amount");
        require(amount > 0, "Amount sent must match the deposit amount");
        balanceOf[msg.sender] += amount;
    }

    function withdraw(uint256 amount) public {
        require(amount <= balanceOf[msg.sender], "Insufficient balance");
        balanceOf[msg.sender] -= amount;
        // payable(msg.sender).transfer(amount);
    }

    function getBalance() public view returns (uint256) {
        return balanceOf[msg.sender];
    }
}