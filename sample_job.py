from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

def run_bell_job():
    print("Connecting to IBM Quantum...")
    service = QiskitRuntimeService(channel="ibm_quantum_platform")
    backend = service.backend("ibm_torino")
    print(f"✅ Successfully connected to backend: {backend.name}")

    print("\nBuilding Bell state circuit...")
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()

    print("Transpiling circuit for the hardware...")
    qc = transpile(qc, backend)

    print("\n--- 🚀 Running Job ---")
    sampler = SamplerV2(backend)
    job = sampler.run([qc])
    print("Job submitted! Job ID:", job.job_id())

    # Wait for result
    result = job.result()
    counts = result[0].data.meas.get_counts()
    print("Result counts:", counts)

    return {
        "job_id": job.job_id(),
        "backend": backend.name,
        "status": str(job.status()),
        "counts": counts
    }