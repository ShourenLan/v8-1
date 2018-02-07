# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "SHORT_EXTERNAL_STRING_TYPE",
  106: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_DOUBLE_ARRAY_TYPE",
  149: "FILLER_TYPE",
  150: "ACCESS_CHECK_INFO_TYPE",
  151: "ACCESSOR_INFO_TYPE",
  152: "ACCESSOR_PAIR_TYPE",
  153: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  154: "ALLOCATION_MEMENTO_TYPE",
  155: "ALLOCATION_SITE_TYPE",
  156: "ASYNC_GENERATOR_REQUEST_TYPE",
  157: "CONTEXT_EXTENSION_TYPE",
  158: "DEBUG_INFO_TYPE",
  159: "FUNCTION_TEMPLATE_INFO_TYPE",
  160: "INTERCEPTOR_INFO_TYPE",
  161: "MODULE_INFO_ENTRY_TYPE",
  162: "MODULE_TYPE",
  163: "OBJECT_TEMPLATE_INFO_TYPE",
  164: "PROMISE_REACTION_JOB_INFO_TYPE",
  165: "PROMISE_RESOLVE_THENABLE_JOB_INFO_TYPE",
  166: "PROTOTYPE_INFO_TYPE",
  167: "SCRIPT_TYPE",
  168: "STACK_FRAME_INFO_TYPE",
  169: "TUPLE2_TYPE",
  170: "TUPLE3_TYPE",
  171: "FIXED_ARRAY_TYPE",
  172: "DESCRIPTOR_ARRAY_TYPE",
  173: "HASH_TABLE_TYPE",
  174: "TRANSITION_ARRAY_TYPE",
  175: "CELL_TYPE",
  176: "CODE_DATA_CONTAINER_TYPE",
  177: "FEEDBACK_VECTOR_TYPE",
  178: "LOAD_HANDLER_TYPE",
  179: "PROPERTY_ARRAY_TYPE",
  180: "PROPERTY_CELL_TYPE",
  181: "SHARED_FUNCTION_INFO_TYPE",
  182: "SMALL_ORDERED_HASH_MAP_TYPE",
  183: "SMALL_ORDERED_HASH_SET_TYPE",
  184: "STORE_HANDLER_TYPE",
  185: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_TYPE",
  1061: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1062: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1063: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1064: "JS_DATE_TYPE",
  1065: "JS_ERROR_TYPE",
  1066: "JS_GENERATOR_OBJECT_TYPE",
  1067: "JS_MAP_TYPE",
  1068: "JS_MAP_KEY_ITERATOR_TYPE",
  1069: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1070: "JS_MAP_VALUE_ITERATOR_TYPE",
  1071: "JS_MESSAGE_OBJECT_TYPE",
  1072: "JS_PROMISE_TYPE",
  1073: "JS_REGEXP_TYPE",
  1074: "JS_SET_TYPE",
  1075: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1076: "JS_SET_VALUE_ITERATOR_TYPE",
  1077: "JS_STRING_ITERATOR_TYPE",
  1078: "JS_WEAK_MAP_TYPE",
  1079: "JS_WEAK_SET_TYPE",
  1080: "JS_TYPED_ARRAY_TYPE",
  1081: "JS_DATA_VIEW_TYPE",
  1082: "JS_TYPED_ARRAY_KEY_ITERATOR_TYPE",
  1083: "JS_FAST_ARRAY_KEY_ITERATOR_TYPE",
  1084: "JS_GENERIC_ARRAY_KEY_ITERATOR_TYPE",
  1085: "JS_UINT8_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1086: "JS_INT8_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1087: "JS_UINT16_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1088: "JS_INT16_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1089: "JS_UINT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1090: "JS_INT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1091: "JS_FLOAT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1092: "JS_FLOAT64_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1093: "JS_UINT8_CLAMPED_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1094: "JS_FAST_SMI_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1095: "JS_FAST_HOLEY_SMI_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1096: "JS_FAST_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1097: "JS_FAST_HOLEY_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1098: "JS_FAST_DOUBLE_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1099: "JS_FAST_HOLEY_DOUBLE_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1100: "JS_GENERIC_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  1101: "JS_UINT8_ARRAY_VALUE_ITERATOR_TYPE",
  1102: "JS_INT8_ARRAY_VALUE_ITERATOR_TYPE",
  1103: "JS_UINT16_ARRAY_VALUE_ITERATOR_TYPE",
  1104: "JS_INT16_ARRAY_VALUE_ITERATOR_TYPE",
  1105: "JS_UINT32_ARRAY_VALUE_ITERATOR_TYPE",
  1106: "JS_INT32_ARRAY_VALUE_ITERATOR_TYPE",
  1107: "JS_FLOAT32_ARRAY_VALUE_ITERATOR_TYPE",
  1108: "JS_FLOAT64_ARRAY_VALUE_ITERATOR_TYPE",
  1109: "JS_UINT8_CLAMPED_ARRAY_VALUE_ITERATOR_TYPE",
  1110: "JS_FAST_SMI_ARRAY_VALUE_ITERATOR_TYPE",
  1111: "JS_FAST_HOLEY_SMI_ARRAY_VALUE_ITERATOR_TYPE",
  1112: "JS_FAST_ARRAY_VALUE_ITERATOR_TYPE",
  1113: "JS_FAST_HOLEY_ARRAY_VALUE_ITERATOR_TYPE",
  1114: "JS_FAST_DOUBLE_ARRAY_VALUE_ITERATOR_TYPE",
  1115: "JS_FAST_HOLEY_DOUBLE_ARRAY_VALUE_ITERATOR_TYPE",
  1116: "JS_GENERIC_ARRAY_VALUE_ITERATOR_TYPE",
  1117: "WASM_INSTANCE_TYPE",
  1118: "WASM_MEMORY_TYPE",
  1119: "WASM_MODULE_TYPE",
  1120: "WASM_TABLE_TYPE",
  1121: "JS_BOUND_FUNCTION_TYPE",
  1122: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  0x02201: (138, "FreeSpaceMap"),
  0x02251: (132, "MetaMap"),
  0x022a1: (131, "NullMap"),
  0x022f1: (172, "DescriptorArrayMap"),
  0x02341: (171, "FixedArrayMap"),
  0x02391: (149, "OnePointerFillerMap"),
  0x023e1: (149, "TwoPointerFillerMap"),
  0x02431: (131, "UninitializedMap"),
  0x02481: (8, "OneByteInternalizedStringMap"),
  0x024d1: (131, "UndefinedMap"),
  0x02521: (129, "HeapNumberMap"),
  0x02571: (131, "TheHoleMap"),
  0x025c1: (131, "BooleanMap"),
  0x02611: (136, "ByteArrayMap"),
  0x02661: (171, "FixedCOWArrayMap"),
  0x026b1: (173, "HashTableMap"),
  0x02701: (128, "SymbolMap"),
  0x02751: (72, "OneByteStringMap"),
  0x027a1: (171, "ScopeInfoMap"),
  0x027f1: (181, "SharedFunctionInfoMap"),
  0x02841: (133, "CodeMap"),
  0x02891: (171, "FunctionContextMap"),
  0x028e1: (175, "CellMap"),
  0x02931: (185, "WeakCellMap"),
  0x02981: (180, "GlobalPropertyCellMap"),
  0x029d1: (135, "ForeignMap"),
  0x02a21: (174, "TransitionArrayMap"),
  0x02a71: (177, "FeedbackVectorMap"),
  0x02ac1: (131, "ArgumentsMarkerMap"),
  0x02b11: (131, "ExceptionMap"),
  0x02b61: (131, "TerminationExceptionMap"),
  0x02bb1: (131, "OptimizedOutMap"),
  0x02c01: (131, "StaleRegisterMap"),
  0x02c51: (171, "NativeContextMap"),
  0x02ca1: (171, "ModuleContextMap"),
  0x02cf1: (171, "EvalContextMap"),
  0x02d41: (171, "ScriptContextMap"),
  0x02d91: (171, "BlockContextMap"),
  0x02de1: (171, "CatchContextMap"),
  0x02e31: (171, "WithContextMap"),
  0x02e81: (171, "DebugEvaluateContextMap"),
  0x02ed1: (171, "ScriptContextTableMap"),
  0x02f21: (171, "ArrayListMap"),
  0x02f71: (148, "FixedDoubleArrayMap"),
  0x02fc1: (134, "MutableHeapNumberMap"),
  0x03011: (173, "OrderedHashMapMap"),
  0x03061: (173, "OrderedHashSetMap"),
  0x030b1: (173, "NameDictionaryMap"),
  0x03101: (173, "GlobalDictionaryMap"),
  0x03151: (173, "NumberDictionaryMap"),
  0x031a1: (173, "SimpleNumberDictionaryMap"),
  0x031f1: (173, "StringTableMap"),
  0x03241: (173, "WeakHashTableMap"),
  0x03291: (171, "SloppyArgumentsElementsMap"),
  0x032e1: (182, "SmallOrderedHashMapMap"),
  0x03331: (183, "SmallOrderedHashSetMap"),
  0x03381: (176, "CodeDataContainerMap"),
  0x033d1: (1071, "JSMessageObjectMap"),
  0x03421: (1057, "ExternalMap"),
  0x03471: (137, "BytecodeArrayMap"),
  0x034c1: (171, "ModuleInfoMap"),
  0x03511: (175, "NoClosuresCellMap"),
  0x03561: (175, "OneClosureCellMap"),
  0x035b1: (175, "ManyClosuresCellMap"),
  0x03601: (179, "PropertyArrayMap"),
  0x03651: (130, "BigIntMap"),
  0x036a1: (106, "NativeSourceStringMap"),
  0x036f1: (64, "StringMap"),
  0x03741: (73, "ConsOneByteStringMap"),
  0x03791: (65, "ConsStringMap"),
  0x037e1: (77, "ThinOneByteStringMap"),
  0x03831: (69, "ThinStringMap"),
  0x03881: (67, "SlicedStringMap"),
  0x038d1: (75, "SlicedOneByteStringMap"),
  0x03921: (66, "ExternalStringMap"),
  0x03971: (82, "ExternalStringWithOneByteDataMap"),
  0x039c1: (74, "ExternalOneByteStringMap"),
  0x03a11: (98, "ShortExternalStringMap"),
  0x03a61: (114, "ShortExternalStringWithOneByteDataMap"),
  0x03ab1: (0, "InternalizedStringMap"),
  0x03b01: (2, "ExternalInternalizedStringMap"),
  0x03b51: (18, "ExternalInternalizedStringWithOneByteDataMap"),
  0x03ba1: (10, "ExternalOneByteInternalizedStringMap"),
  0x03bf1: (34, "ShortExternalInternalizedStringMap"),
  0x03c41: (50, "ShortExternalInternalizedStringWithOneByteDataMap"),
  0x03c91: (42, "ShortExternalOneByteInternalizedStringMap"),
  0x03ce1: (106, "ShortExternalOneByteStringMap"),
  0x03d31: (140, "FixedUint8ArrayMap"),
  0x03d81: (139, "FixedInt8ArrayMap"),
  0x03dd1: (142, "FixedUint16ArrayMap"),
  0x03e21: (141, "FixedInt16ArrayMap"),
  0x03e71: (144, "FixedUint32ArrayMap"),
  0x03ec1: (143, "FixedInt32ArrayMap"),
  0x03f11: (145, "FixedFloat32ArrayMap"),
  0x03f61: (146, "FixedFloat64ArrayMap"),
  0x03fb1: (147, "FixedUint8ClampedArrayMap"),
  0x04001: (169, "Tuple2Map"),
  0x04051: (167, "ScriptMap"),
  0x040a1: (160, "InterceptorInfoMap"),
  0x040f1: (151, "AccessorInfoMap"),
  0x04141: (150, "AccessCheckInfoMap"),
  0x04191: (152, "AccessorPairMap"),
  0x041e1: (153, "AliasedArgumentsEntryMap"),
  0x04231: (154, "AllocationMementoMap"),
  0x04281: (155, "AllocationSiteMap"),
  0x042d1: (156, "AsyncGeneratorRequestMap"),
  0x04321: (157, "ContextExtensionMap"),
  0x04371: (158, "DebugInfoMap"),
  0x043c1: (159, "FunctionTemplateInfoMap"),
  0x04411: (161, "ModuleInfoEntryMap"),
  0x04461: (162, "ModuleMap"),
  0x044b1: (163, "ObjectTemplateInfoMap"),
  0x04501: (164, "PromiseReactionJobInfoMap"),
  0x04551: (165, "PromiseResolveThenableJobInfoMap"),
  0x045a1: (166, "PrototypeInfoMap"),
  0x045f1: (168, "StackFrameInfoMap"),
  0x04641: (170, "Tuple3Map"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("OLD_SPACE", 0x02201): "NullValue",
  ("OLD_SPACE", 0x02231): "EmptyDescriptorArray",
  ("OLD_SPACE", 0x02251): "EmptyFixedArray",
  ("OLD_SPACE", 0x02261): "UninitializedValue",
  ("OLD_SPACE", 0x022e1): "UndefinedValue",
  ("OLD_SPACE", 0x02311): "NanValue",
  ("OLD_SPACE", 0x02321): "TheHoleValue",
  ("OLD_SPACE", 0x02371): "HoleNanValue",
  ("OLD_SPACE", 0x02381): "TrueValue",
  ("OLD_SPACE", 0x023f1): "FalseValue",
  ("OLD_SPACE", 0x02441): "empty_string",
  ("OLD_SPACE", 0x02459): "EmptyScopeInfo",
  ("OLD_SPACE", 0x02469): "ArgumentsMarker",
  ("OLD_SPACE", 0x024c1): "Exception",
  ("OLD_SPACE", 0x02519): "TerminationException",
  ("OLD_SPACE", 0x02579): "OptimizedOut",
  ("OLD_SPACE", 0x025d1): "StaleRegister",
  ("OLD_SPACE", 0x02651): "EmptyByteArray",
  ("OLD_SPACE", 0x02661): "EmptyFixedUint8Array",
  ("OLD_SPACE", 0x02681): "EmptyFixedInt8Array",
  ("OLD_SPACE", 0x026a1): "EmptyFixedUint16Array",
  ("OLD_SPACE", 0x026c1): "EmptyFixedInt16Array",
  ("OLD_SPACE", 0x026e1): "EmptyFixedUint32Array",
  ("OLD_SPACE", 0x02701): "EmptyFixedInt32Array",
  ("OLD_SPACE", 0x02721): "EmptyFixedFloat32Array",
  ("OLD_SPACE", 0x02741): "EmptyFixedFloat64Array",
  ("OLD_SPACE", 0x02761): "EmptyFixedUint8ClampedArray",
  ("OLD_SPACE", 0x02781): "EmptyScript",
  ("OLD_SPACE", 0x02809): "UndefinedCell",
  ("OLD_SPACE", 0x02819): "EmptySloppyArgumentsElements",
  ("OLD_SPACE", 0x02839): "EmptySlowElementDictionary",
  ("OLD_SPACE", 0x02881): "EmptyOrderedHashMap",
  ("OLD_SPACE", 0x028a9): "EmptyOrderedHashSet",
  ("OLD_SPACE", 0x028d1): "EmptyPropertyCell",
  ("OLD_SPACE", 0x028f9): "EmptyWeakCell",
  ("OLD_SPACE", 0x02969): "NoElementsProtector",
  ("OLD_SPACE", 0x02991): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x029a1): "SpeciesProtector",
  ("OLD_SPACE", 0x029c9): "StringLengthProtector",
  ("OLD_SPACE", 0x029d9): "FastArrayIterationProtector",
  ("OLD_SPACE", 0x029e9): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x02a11): "ArrayBufferNeuteringProtector",
  ("OLD_SPACE", 0x02a61): "InfinityValue",
  ("OLD_SPACE", 0x02a71): "MinusZeroValue",
  ("OLD_SPACE", 0x02a81): "MinusInfinityValue",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "WASM_TO_WASM",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
