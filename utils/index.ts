import fs from 'fs/promises';

const main = async () => {

  const response = await fetch('https://gob-do-api.www.gob.do/api/v2/portals/services')
  const data = await response.json();

  const cleanData = data.data.map((item: any) => {
    return {
      name: item.service_name,
      description: item.service_name,
      slug: item.slug,
      type: item.service_type,
      institutionName: item.institution_name,
      institutionPhone: item.institution_phone,
    }
  }
  );

  console.log(cleanData);

  // save to file
  await fs.writeFile('../data.json', JSON.stringify(cleanData, null, 2));
};

main();