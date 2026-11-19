class RuleBasedSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_rule(self, antecedent, consequent):
        self.rules.append((antecedent, consequent))

    def add_fact(self, fact):
        self.facts.add(fact)

    def forward_chain(self):
        new_fact_found = True
        while new_fact_found:
            new_fact_found = False
            for ante, cons in self.rules:
                if isinstance(ante, list):
                    condition_met = all( condition in self.facts for condition in ante)
                else: 
                    condition_met = ante in self.facts

                if condition_met and cons not in self.facts:
                    self.facts.add(cons)
                    new_fact_found = True

                    print(f"Inferred new fact: {cons}")

        print("\nInference complete. Final facts:")

        for fact in sorted(self.facts):
            print(f"- {fact}")

if __name__ == "__main__":
    system = RuleBasedSystem()
    # Add rules
    system.add_rule("has_fur", "is_mammal")
    system.add_rule(["is_mammal", "eats_meat"],"is_carnivore")
    system.add_rule(["is_carnivore", "has_black_stripes", "has_tawny_color"], "is_tiger")
    system.add_rule("is_tiger","is_animal")
    
    system.add_fact("has_fur")
    system.add_fact("eats_meat") 
    system.add_fact("has_tawny_color")
    system.add_fact("has_black_stripes")

    system.forward_chain()
