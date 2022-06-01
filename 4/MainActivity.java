package com.yrx4;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.LibraryResolver;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.DalvikModule;
import com.github.unidbg.linux.android.dvm.DvmObject;
import com.github.unidbg.linux.android.dvm.StringObject;
import com.github.unidbg.linux.android.dvm.VM;
import com.github.unidbg.memory.Memory;

import java.io.File;

public class MainActivity {
    private final DvmObject<?> dvmObject;

    public String GetSign(String input_str, long j) {
        StringObject stringObject = new StringObject(vm, input_str);
        //查找的方法 不要忘记;号
        String sign_str = dvmObject.callJniMethodObject(emulator, "sign(Ljava/lang/String;J)Ljava/lang/String;", stringObject, j).getValue().toString();
        return sign_str;
    }

    private final AndroidEmulator emulator;
    private final VM vm;

    public MainActivity() {
        emulator = AndroidEmulatorBuilder
                .for64Bit()
                .build();
        Memory memory = emulator.getMemory();
        LibraryResolver resolver = new AndroidResolver(23);
        memory.setLibraryResolver(resolver);

        vm = emulator.createDalvikVM();
        vm.setVerbose(false); //是否输出日志
        DalvikModule dm = vm.loadLibrary(new File(getPath() + "/yrx4/libmatch04.so"), false);
        dm.callJNI_OnLoad(emulator);
        dvmObject = vm.resolveClass("com.yuanrenxue.match2022.fragment.challenge.ChallengeFourFragment".replace(".", "/")).newObject(null);
    }

    public String getPath() {
        String path = this.getClass().getProtectionDomain().getCodeSource().getLocation().getPath();
        if (System.getProperty("os.name").contains("dows")) {
            path = path.substring(1, path.length());
        }
        if (path.contains("jar")) {
            // System.out.println("jar = " + path);
            path = path.substring(0, path.lastIndexOf("."));
            return path.substring(0, path.lastIndexOf("/"));
        }

        // System.out.println(path);
        // path.replace("target/classes/", "");
        return path.replace("/target/test-classes/", "/src/test/java/com");
    }

    public static void main(String[] args) {
        MainActivity sign_func = new MainActivity();
        System.out.println(sign_func.GetSign("1:1653459592555", 1653459592555L));

    }
}
