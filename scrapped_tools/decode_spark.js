const protobuf = require('C:/Users/chris/.gemini/antigravity/brain/4621470a-fbef-4973-848e-5f18970291b3/node_modules/protobufjs');
const fs = require('fs');

async function main() {
    const root = await protobuf.load('C:/Users/chris/.gemini/antigravity/brain/4621470a-fbef-4973-848e-5f18970291b3/spark.proto');
    const SamplerData = root.lookupType('spark.SamplerData');
    const profileId = process.argv[2] || 'Ls38V4SVns';
    const buffer = fs.readFileSync(`C:/Users/chris/.gemini/antigravity/brain/4621470a-fbef-4973-848e-5f18970291b3/spark_${profileId}.pb`);
    const data = SamplerData.toObject(SamplerData.decode(buffer), { longs: Number, defaults: true });
    
    console.log('=== METRICS ===');
    console.log('Ticks:', data.metadata?.numberOfTicks);
    const durMs = (data.metadata?.endTime - data.metadata?.startTime);
    console.log('Duration:', (durMs / 1000).toFixed(1), 's');
    if (data.timeWindowStatistics) {
        for (const [k, v] of Object.entries(data.timeWindowStatistics)) {
            console.log(`Window ${k}: TPS=${v.tps?.toFixed(1)}, MSPT median=${v.msptMedian?.toFixed(2)}, max=${v.msptMax?.toFixed(2)}, CPU proc=${v.cpuProcess?.toFixed(1)}%, entities=${v.entities}, chunks=${v.chunks}`);
        }
    }
    
    const serverThread = data.threads.find(t => t.name.includes('Server thread')) || data.threads[0];
    const allNodes = serverThread.children;
    const classSources = data.classSources || {};
    
    function getNodeTime(n) {
        if (!n) return 0;
        return (n.times && n.times.length > 0) ? n.times.reduce((a, b) => a + b, 0) : (n.time || 0);
    }
    
    const totalTime = getNodeTime(allNodes[serverThread.childrenRefs[0]]);
    console.log('\nServer thread total time:', totalTime);
    
    const lines = [];
    
    function walk(idx, depth) {
        if (idx >= allNodes.length) return;
        const node = allNodes[idx];
        const time = getNodeTime(node);
        const pct = (time / totalTime) * 100;
        if (pct < 0.2) return;
        
        const cName = node.className || '';
        const mName = node.methodName || '';
        const modId = classSources[cName] || '';
        const modStr = modId ? '[' + modId + '] ' : '';
        const indent = '  '.repeat(depth);
        lines.push(pct.toFixed(2).padStart(6) + '% ' + indent + modStr + cName + '.' + mName + (node.lineNumber ? ':' + node.lineNumber : ''));
        
        const childRefs = node.childrenRefs || [];
        const sortedChildren = [...childRefs].sort((a, b) => getNodeTime(allNodes[b]) - getNodeTime(allNodes[a]));
        
        for (const childIdx of sortedChildren) {
            walk(childIdx, depth + 1);
        }
    }
    
    for (const rootIdx of serverThread.childrenRefs) {
        walk(rootIdx, 0);
    }
    
    fs.writeFileSync(`C:/Users/chris/.gemini/antigravity/brain/4621470a-fbef-4973-848e-5f18970291b3/flametree_${profileId}.txt`, lines.join('\n'));
    console.log(`Wrote flametree_${profileId}.txt, total lines:`, lines.length);
}

main().catch(console.error);
