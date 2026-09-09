# Data Refactoring Log

## Project

This project refactors the student records system from the earlier module.
The original file was not modified. The refactored version is stored in
`refactored_data.py`.

## 1. Students Collection

### Original structure

The original program used a list called `students`.

### Chosen structure

The refactored program keeps `students` as a list.

### Justification

A list is appropriate because the program stores multiple student records
in an ordered collection. Students can be added using `append()`, and the
program can loop through the records in their stored order.

### What would break if another structure were used?

A set would not be appropriate because it does not preserve the same
ordered-record behavior and is not necessary for this program. A dictionary
would require a key for every student and would change how the records are
stored and accessed.

---

## 2. Individual Student Records

### Original structure

The original program used a namedtuple called `Student`.

### Chosen structure

The refactored program keeps `Student` as a namedtuple with the fields:

- `name`
- `age`
- `grade`

### Justification

A namedtuple is appropriate because every student has the same fixed fields.
The fields can be accessed by meaningful names, such as `student.name` and
`student.grade`, instead of using positions such as `student[0]`.

Namedtuples are also immutable. This is useful because a student record
should not be changed accidentally after it has been created.

### What would break if another structure were used?

A normal list would make the fields less meaningful because the program
would need to remember positions. For example, `student[2]` would be less
clear than `student.grade`.

A dictionary would allow fields to be changed freely, which would remove
the immutability demonstration. It could still work, but it would not
provide the same fixed-record behavior.

---

## 3. Contact Fields

### Decision

The student record fields are represented by namedtuple field names:
`name`, `age`, and `grade`.

### Justification

These fields have fixed meanings and are accessed by name. A namedtuple
makes the structure clear and prevents accidental changes to the record.

---

## 4. VALID_GRADES

### Original structure

The original program created a list inside `create_student()`:

```python
valid_grades = ["A", "B", "C", "D", "F"]
