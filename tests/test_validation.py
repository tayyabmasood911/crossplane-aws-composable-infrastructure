import os
import unittest

class TestComponentIntegrity(unittest.TestCase):
    def test_readme_exists(self):
        self.assertTrue(os.path.exists("README.md"), "README.md must be present")

    def test_makefile_exists(self):
        self.assertTrue(os.path.exists("Makefile"), "Makefile must be present")

    def test_ci_workflow_exists(self):
        self.assertTrue(os.path.exists(".github/workflows/ci.yml"), "CI workflow must be present")

    def test_healthcheck_script_exists(self):
        self.assertTrue(os.path.exists("scripts/healthcheck.sh"), "Healthcheck script must be present")

    def test_environment_template_exists(self):
        self.assertTrue(os.path.exists("config/production.env.example"), "Env template must be present")

    def test_gitattributes_exists(self):
        self.assertTrue(os.path.exists(".gitattributes"), ".gitattributes must be present")

    def test_security_policy_exists(self):
        self.assertTrue(os.path.exists("SECURITY.md"), "SECURITY.md must be present")

    def test_architecture_svg_exists(self):
        self.assertTrue(os.path.exists("docs/architecture.svg"), "docs/architecture.svg must be present")
        with open("docs/architecture.svg", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("#ffffff", content, "Architecture SVG must have strict white background")
            self.assertIn("<svg", content, "Valid SVG root element required")

    def test_crossplane_manifests(self):
        manifests = [
            "crossplane.yaml",
            "definition.yaml",
            "composition.yaml",
            "apis/network/definition.yaml",
            "apis/network/composition.yaml",
            "apis/database/definition.yaml",
            "apis/database/composition.yaml",
            "apis/storage/definition.yaml",
            "apis/storage/composition.yaml",
            "examples/claims/network-claim.yaml",
            "examples/claims/database-claim.yaml",
            "examples/claims/storage-claim.yaml"
        ]
        for m in manifests:
            self.assertTrue(os.path.exists(m), f"Crossplane manifest {m} must be present")
            with open(m, "r", encoding="utf-8") as f:
                self.assertGreater(len(f.read().strip()), 0, f"Manifest {m} must not be empty")

if __name__ == "__main__":
    unittest.main()
