package multithreading;

import java.util.concurrent.atomic.*;

/**
 * Main
 */

class Employee
{
    public int id;
    public String name;

    // constructor & getters & setters
    public Employee(int id, String name)
    {
        this.id = id;
        this.name = name;
    }
}

public class AtomicMarkableReferenceExample
{
    public static void main(String[] args)
    {
        Employee employee = new Employee(123, "Mike");
        AtomicMarkableReference<Employee> employeeNode = new AtomicMarkableReference<>(employee, true);

        assert employee == employeeNode.getReference();
        assert employeeNode.isMarked();

        // #region get()
        // boolean[] markHolder = new boolean[1];
        // Employee currentEmployee = employeeNode.get(markHolder);
        // System.out.println(employee.id + " " + employee.name);
        // System.out.println(currentEmployee.id + " " + currentEmployee.name);
        // assert employee == currentEmployee;
        // assert markHolder[0];
        //#endregion

        //#region set()
        Employee newEmployee = new Employee(124, "John");
        employeeNode.set(newEmployee, false);

        assert newEmployee == employeeNode.getReference();
        assert !employeeNode.isMarked();

        //#endregion

        //#region compare and set()
        // Employee employee = new Employee(123, "Mike");
        // AtomicMarkableReference<Employee> employeeNode = new AtomicMarkableReference<>(employee, true);
        // Employee newEmployee = new Employee(124, "John");

        // Assertions.assertTrue(employeeNode.compareAndSet(employee, newEmployee, true, false));
        // Assertions.assertEquals(newEmployee, employeeNode.getReference());
        // Assertions.assertFalse(employeeNode.isMarked());
        //#endregion

        // #region weakCAS()
        // typically used inside a loop to save memory
        //#endregion

        //#region attemptMark()
        // Employee employee = new Employee(123, "Mike");
        // AtomicMarkableReference<Employee> employeeNode = new AtomicMarkableReference<>(employee, true);

        // Assertions.assertTrue(employeeNode.attemptMark(employee, false));
        // Assertions.assertFalse(employeeNode.isMarked());
        //#endregion



    }

}