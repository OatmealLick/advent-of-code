#import "Basic";
#import "Machine_X64";

estimate_cpu_frequency :: (millis_to_wait: int = 100) -> u64 {
    nanos_to_wait := 1000_000 * millis_to_wait;

    apollo_start := current_time_consensus();
    cpu_start := rdtsc();

    apollo_end := current_time_consensus();
    elapsed_nanos := to_nanoseconds(apollo_end - apollo_start);
    while elapsed_nanos < nanos_to_wait {
	apollo_end = current_time_consensus();
	elapsed_nanos = to_nanoseconds(apollo_end - apollo_start);
    }
    cpu_end := rdtsc();
    elapsed_ticks := cpu_end - cpu_start;
    cpu_freq_in_ghz := cast(float64) elapsed_ticks / (elapsed_nanos);
    return cast(u64) (cpu_freq_in_ghz * 1_000_000_000);
}

