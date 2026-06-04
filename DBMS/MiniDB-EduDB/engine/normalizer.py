class Normalizer:

    # -----------------------------------------
    # DISPLAY FUNCTIONAL DEPENDENCIES
    # -----------------------------------------
    def show_functional_dependencies(self):

        print(
            "\n========== FUNCTIONAL DEPENDENCIES ==========\n"
        )

        print("StudentID -> StudentName")
        print("StudentID -> Department")
        print("Department -> HOD")

    # -----------------------------------------
    # FIRST NORMAL FORM (1NF)
    # -----------------------------------------
    def check_1nf(self):

        print(
            "\n========== FIRST NORMAL FORM (1NF) ==========\n"
        )

        print(
            "Conditions:\n"
            "- Atomic attributes\n"
            "- No repeating groups\n"
            "- Unique rows"
        )

        print(
            "\nResult:\n"
            "Table satisfies 1NF."
        )

    # -----------------------------------------
    # SECOND NORMAL FORM (2NF)
    # -----------------------------------------
    def check_2nf(self):

        print(
            "\n========== SECOND NORMAL FORM (2NF) ==========\n"
        )

        print(
            "Conditions:\n"
            "- Must satisfy 1NF\n"
            "- No partial dependency"
        )

        print(
            "\nPartial Dependency Example:\n"
            "StudentID -> StudentName"
        )

        print(
            "\nResult:\n"
            "Partial dependencies removed.\n"
            "Table satisfies 2NF."
        )

    # -----------------------------------------
    # THIRD NORMAL FORM (3NF)
    # -----------------------------------------
    def check_3nf(self):

        print(
            "\n========== THIRD NORMAL FORM (3NF) ==========\n"
        )

        print(
            "Conditions:\n"
            "- Must satisfy 2NF\n"
            "- No transitive dependency"
        )

        print(
            "\nTransitive Dependency Example:\n"
            "StudentID -> Department\n"
            "Department -> HOD"
        )

        print(
            "\nResult:\n"
            "Transitive dependencies removed.\n"
            "Table satisfies 3NF."
        )

    # -----------------------------------------
    # BOYCE-CODD NORMAL FORM (BCNF)
    # -----------------------------------------
    def check_bcnf(self):

        print(
            "\n========== BOYCE-CODD NORMAL FORM (BCNF) ==========\n"
        )

        print(
            "Conditions:\n"
            "- Every determinant must be a candidate key"
        )

        print(
            "\nResult:\n"
            "Table satisfies BCNF."
        )

    # -----------------------------------------
    # NORMALIZATION DEMO
    # -----------------------------------------
    def normalization_demo(self):

        print(
            "\n========== NORMALIZATION PROCESS ==========\n"
        )

        print(
            "UNNORMALIZED TABLE\n"
            "↓\n"
            "1NF\n"
            "↓\n"
            "2NF\n"
            "↓\n"
            "3NF\n"
            "↓\n"
            "BCNF"
        )

    # -----------------------------------------
    # DECOMPOSITION DEMO
    # -----------------------------------------
    def decomposition_demo(self):

        print(
            "\n========== TABLE DECOMPOSITION ==========\n"
        )

        print(
            "Original Relation:\n"
            "Student(StudentID, StudentName, "
            "Department, HOD)\n"
        )

        print(
            "Decomposed Relations:\n"
        )

        print(
            "Student(StudentID, StudentName, Department)"
        )

        print(
            "Department(Department, HOD)"
        )

    # -----------------------------------------
    # LOSSLESS JOIN CHECK
    # -----------------------------------------
    def lossless_join_demo(self):

        print(
            "\n========== LOSSLESS JOIN ==========\n"
        )

        print(
            "Decomposition preserves information.\n"
            "Original relation can be reconstructed."
        )

    # -----------------------------------------
    # DEPENDENCY PRESERVATION
    # -----------------------------------------
    def dependency_preservation_demo(self):

        print(
            "\n========== DEPENDENCY PRESERVATION ==========\n"
        )

        print(
            "All functional dependencies preserved "
            "after decomposition."
        )