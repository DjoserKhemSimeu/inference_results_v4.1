# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4(OfflineGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx4
    gpu_batch_size = {'gptj': 100}
    use_fp8 = True
    offline_expected_qps = 10*4
    enable_sort = False

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4_HighAccuracy(HPE_ProLiant_DL380a_L40S_PCIe_48GBx4):
    pass

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4(H100_PCIe_80GBx1):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_PCIe_80GBx4
    offline_expected_qps = 25 * 4 #16 * 4
    gpu_batch_size = {'gptj': 192}

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4_HighAccuracy(HPE_ProLiant_DL380a_H100_PCIe_80GBx4):
    pass

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4(OfflineGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_NVL_94GBx4
    gpu_batch_size = {'gptj': 192}
    use_fp8 = True
    offline_expected_qps = 30 * 4 #25 * 4 - valid
    enable_sort = False

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4_HighAccuracy(HPE_PROLIANT_DL380A_H100_NVL_94GBX4):
    pass

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8(H100_SXM_80GBx8):
    system = KnownSystem.HPE_Cray_XD670_H100_SXM_80GBx8
    gpu_batch_size = {'gptj': 256} #192
    offline_expected_qps = 244 #30.5*8

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8_HighAccuracy(HPE_CRAY_XD670_H100_SXM_80GBX8):
    pass

"""
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
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    coalesced_tensor: bool = False
    enable_sort: bool = False
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    instance_group_count: int = 0
    kvcache_free_gpu_mem_frac: float = 0.0
    llm_gen_config_path: str = ''
    max_num_tokens: int = 0
    model_path: str = ''
    num_sort_segments: int = 0
    numa_config: str = ''
    offline_expected_qps: float = 0.0
    performance_sample_count_override: int = 0
    pipeline_parallelism: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    tensor_parallelism: int = 0
    trtllm_batch_sched_policy: str = ''
    trtllm_batching_mode: str = ''
    use_fp8: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_spin_wait: bool = False
    use_token_latencies: bool = False
    vboost_slider: int = 0
    verbose_glog: int = 0
    workspace_size: int = 0
"""



