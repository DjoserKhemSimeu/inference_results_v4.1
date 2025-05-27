# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ORIN(OfflineGPUBaseConfig):
    system = KnownSystem.Orin

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: Dict = {}
    input_dtype: str = ''
    input_format: str = ''
    precision: str = ''
    tensor_path: str = ''

    # Optional fields:
    active_sms: int = 0
    bot_mlp_precision: str = ''
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    check_contiguity: bool = False
    coalesced_tensor: bool = False
    complete_threads: int = 0
    embedding_weights_on_gpu_part: float = 0.0
    embeddings_path: str = ''
    embeddings_precision: str = ''
    final_linear_precision: str = ''
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    gpu_num_bundles: int = 0
    instance_group_count: int = 0
    interaction_op_precision: str = ''
    max_pairs_per_staging_thread: int = 0
    model_path: str = ''
    num_staging_batches: int = 0
    num_staging_threads: int = 0
    offline_expected_qps: float = 0.0
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    qsl_numa_override: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    sample_partition_path: str = ''
    top_mlp_precision: str = ''
    use_batcher_thread_per_device: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_spin_wait: bool = False
    vboost_slider: int = 0
    verbose_glog: int = 0
    warmup_duration: float = 0.0
    workspace_size: int = 0


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ORIN_HighAccuracy(ORIN):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class ORIN_Triton(ORIN):
    use_triton = True

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: Dict = {}
    input_dtype: str = ''
    input_format: str = ''
    precision: str = ''
    tensor_path: str = ''

    # Optional fields:
    active_sms: int = 0
    batch_triton_requests: bool = False
    bot_mlp_precision: str = ''
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    check_contiguity: bool = False
    coalesced_tensor: bool = False
    complete_threads: int = 0
    dla_num_batchers: int = 0
    dla_num_issuers: int = 0
    embedding_weights_on_gpu_part: float = 0.0
    embeddings_path: str = ''
    embeddings_precision: str = ''
    final_linear_precision: str = ''
    gather_kernel_buffer_threshold: int = 0
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    gpu_num_bundles: int = 0
    instance_group_count: int = 0
    interaction_op_precision: str = ''
    max_pairs_per_staging_thread: int = 0
    max_queue_delay_usec: int = 0
    model_path: str = ''
    num_concurrent_batchers: int = 0
    num_concurrent_issuers: int = 0
    num_staging_batches: int = 0
    num_staging_threads: int = 0
    offline_expected_qps: float = 0.0
    output_pinned_memory: bool = False
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    qsl_numa_override: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    sample_partition_path: str = ''
    top_mlp_precision: str = ''
    use_batcher_thread_per_device: bool = False
    use_concurrent_harness: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_spin_wait: bool = False
    vboost_slider: int = 0
    verbose_glog: int = 0
    warmup_duration: float = 0.0
    workspace_size: int = 0


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ORIN_HighAccuracy_Triton(ORIN_HighAccuracy):
    use_triton = True


