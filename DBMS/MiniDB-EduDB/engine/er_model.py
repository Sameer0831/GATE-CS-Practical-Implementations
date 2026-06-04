class ERModel:

    # -----------------------------------------
    # DISPLAY ENTITY
    # -----------------------------------------
    def create_entity(self, entity_name, attributes):

        print(
            f"\n========== ENTITY: {entity_name} ==========\n"
        )

        print("Attributes:")

        for attribute in attributes:

            print(f"- {attribute}")

    # -----------------------------------------
    # DISPLAY RELATIONSHIP
    # -----------------------------------------
    def create_relationship(
        self,
        entity1,
        relationship,
        entity2
    ):

        print(
            "\n========== RELATIONSHIP ==========\n"
        )

        print(
            f"{entity1} ---- "
            f"{relationship} ---- "
            f"{entity2}"
        )

    # -----------------------------------------
    # ONE-TO-ONE RELATIONSHIP
    # -----------------------------------------
    def one_to_one(self, entity1, entity2):

        print(
            "\n========== ONE-TO-ONE RELATIONSHIP ==========\n"
        )

        print(
            f"{entity1}  <---->  {entity2}"
        )

    # -----------------------------------------
    # ONE-TO-MANY RELATIONSHIP
    # -----------------------------------------
    def one_to_many(self, entity1, entity2):

        print(
            "\n========== ONE-TO-MANY RELATIONSHIP ==========\n"
        )

        print(
            f"{entity1}  <----  {entity2}"
        )

    # -----------------------------------------
    # MANY-TO-MANY RELATIONSHIP
    # -----------------------------------------
    def many_to_many(self, entity1, entity2):

        print(
            "\n========== MANY-TO-MANY RELATIONSHIP ==========\n"
        )

        print(
            f"{entity1}  >----<  {entity2}"
        )

    # -----------------------------------------
    # WEAK ENTITY
    # -----------------------------------------
    def weak_entity(self, entity_name):

        print(
            "\n========== WEAK ENTITY ==========\n"
        )

        print(
            f"{entity_name} is a weak entity."
        )

    # -----------------------------------------
    # MULTIVALUED ATTRIBUTE
    # -----------------------------------------
    def multivalued_attribute(self, attribute_name):

        print(
            "\n========== MULTIVALUED ATTRIBUTE ==========\n"
        )

        print(
            f"{attribute_name} is a multivalued attribute."
        )

    # -----------------------------------------
    # DERIVED ATTRIBUTE
    # -----------------------------------------
    def derived_attribute(self, attribute_name):

        print(
            "\n========== DERIVED ATTRIBUTE ==========\n"
        )

        print(
            f"{attribute_name} is a derived attribute."
        )

    # -----------------------------------------
    # ER TO RELATIONAL MODEL CONVERSION
    # -----------------------------------------
    def er_to_relational_demo(self):

        print(
            "\n========== ER TO RELATIONAL MAPPING ==========\n"
        )

        print(
            "ER Diagram:\n"
        )

        print(
            "Student ---- Enrolls ---- Course"
        )

        print(
            "\nConverted Relational Schema:\n"
        )

        print(
            "Student(StudentID, StudentName, Department)"
        )

        print(
            "Course(CourseID, CourseName)"
        )

        print(
            "Enrollment(StudentID, CourseID)"
        )

    # -----------------------------------------
    # SPECIALIZATION
    # -----------------------------------------
    def specialization_demo(self):

        print(
            "\n========== SPECIALIZATION ==========\n"
        )

        print(
            "Person\n"
            "  ↓\n"
            "Student\n"
            "Teacher"
        )

    # -----------------------------------------
    # GENERALIZATION
    # -----------------------------------------
    def generalization_demo(self):

        print(
            "\n========== GENERALIZATION ==========\n"
        )

        print(
            "Student\n"
            "Teacher\n"
            "  ↑\n"
            "Person"
        )

    # -----------------------------------------
    # AGGREGATION
    # -----------------------------------------
    def aggregation_demo(self):

        print(
            "\n========== AGGREGATION ==========\n"
        )

        print(
            "Aggregation treats relationships "
            "as higher-level entities."
        )