"""Errors raised by the Axiom compiled-artifact integration."""


class AxiomIntegrationError(RuntimeError):
    """Base class for fail-closed Axiom integration errors."""


class AxiomDependencyError(AxiomIntegrationError):
    """The official Axiom Python package is unavailable."""


class AxiomRuntimeUnavailableError(AxiomIntegrationError):
    """The configured Axiom engine executable cannot be used."""


class AxiomArtifactError(AxiomIntegrationError):
    """A compiled artifact is missing, malformed, or unsupported."""


class AxiomInputCatalogError(AxiomIntegrationError):
    """Runtime inputs do not match the compiled artifact's catalog."""


class AxiomExecutionError(AxiomIntegrationError):
    """The real Axiom engine failed to execute a compiled artifact."""


class AxiomOutputError(AxiomIntegrationError):
    """The engine response does not contain the requested scalar output."""
