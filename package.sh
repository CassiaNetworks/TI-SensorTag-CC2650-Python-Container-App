set -x
version=0.1.0
name=SamplePython3App
build_path=/tmp/build
rm -rf ${build_path}
mkdir -p ${build_path}/${name}.${version}/
npm i
cp -R * ${build_path}/${name}.${version}/

cd ${build_path}
tar -czvf ${name}.${version}.tar.gz ${name}.${version}

cd -
cp ${build_path}/*.tar.gz ../