// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentDataManager {
    // Structure to store student information
    struct Student {
        string name;
        uint256 age;
        uint256 grade;
    }

    // Array to store student records
    Student[] public students;

    // Function to add a new student
    function addStudent(string memory _name, uint256 _age, uint256 _grade) public {
        Student memory newStudent = Student(_name, _age, _grade);
        students.push(newStudent);
    }

    // Function to get the number of students
    function getNumStudents() public view returns (uint256) {
        return students.length;
    }

    // Receive function
    receive() external payable {}

    // Fallback function
    fallback() external payable {}
}